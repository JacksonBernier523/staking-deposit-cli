from utils.crypto import (
    HKDF,
    SHA256,
)
from py_ecc.optimized_bls12_381 import curve_order as bls_curve_order
from typing import List


def _flip_bits_256(input: int) -> int:
    """
    Flips 256 bits worth of `input`.
    """
    return input ^ (2**256 - 1)


def _IKM_to_lamport_SK(*, IKM: bytes, salt: bytes) -> List[bytes]:
    """
    Derives the lamport SK for a given `IKM` and `salt`.
    """
    OKM = HKDF(salt=salt, IKM=IKM, L=8160)
    lamport_SK = [OKM[i: i + 32] for i in range(0, 8160, 32)]
    return lamport_SK


def _parent_SK_to_lamport_PK(*, parent_SK: int, index: int) -> bytes:
    """
    Derives the `index`th child's lamport PK from the `parent_SK`.
    """
    salt = index.to_bytes(4, byteorder='big')
    IKM = parent_SK.to_bytes(32, byteorder='big')
    lamport_0 = _IKM_to_lamport_SK(IKM=IKM, salt=salt)
    not_IKM = _flip_bits_256(parent_SK).to_bytes(32, byteorder='big')
    lamport_1 = _IKM_to_lamport_SK(IKM=not_IKM, salt=salt)
    lamport_SKs = lamport_0 + lamport_1
    lamport_PKs = [SHA256(sk) for sk in lamport_SKs]
    compressed_PK = SHA256(b''.join(lamport_PKs))
    return compressed_PK


def _HKDF_mod_r(*, IKM: bytes) -> int:
    okm = HKDF(salt=b'BLS-SIG-KEYGEN-SALT-', IKM=IKM, L=48)
    return int.from_bytes(okm, byteorder='big') % bls_curve_order


def derive_child_SK(*, parent_SK: int, index: int) -> int:
    assert(index >= 0 and index < 2**32)
    lamport_PK = _parent_SK_to_lamport_PK(parent_SK=parent_SK, index=index)
    return _HKDF_mod_r(IKM=lamport_PK)


def derive_master_SK(seed: bytes) -> int:
    assert(len(seed) >= 16)
    return _HKDF_mod_r(IKM=seed)
