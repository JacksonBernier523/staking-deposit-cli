import os
import json
from py_ecc.bls import G2ProofOfPossession as bls


from eth2deposit.key_handling.key_derivation.tree import (
    _HKDF_mod_r,
    derive_child_SK,
    derive_master_SK,
)


test_vector_filefolder = os.path.join(os.getcwd(), 'tests', 'test_key_handling',
                                      'test_key_derivation', 'test_vectors', 'tree_kdf.json')
with open(test_vector_filefolder, 'r') as f:
    test_vectors = json.load(f)['kdf_tests']


@pytest.mark.parametrize(
    'test',
    test_vectors
)
def test_hkdf_mod_r(test) -> None:
    seed = bytes.fromhex(test['seed'])
    assert bls.KeyGen(seed) == _HKDF_mod_r(IKM=seed)



@pytest.mark.parametrize(
    'test',
    test_vectors
)
def test_derive_master_SK(test) -> None:
    seed = bytes.fromhex(test['seed'])
    master_SK = test['master_SK']
    assert derive_master_SK(seed=seed) == master_SK


@pytest.mark.parametrize(
    'test',
    test_vectors
)
def test_derive_child_SK(test) -> None:
    parent_SK = test['master_SK']
    index = test['child_index']
    child_SK = test['child_SK']
    assert derive_child_SK(parent_SK=parent_SK, index=index) == child_SK
    for test in test_vectors:
        parent_SK = test['master_SK']
        index = test['child_index']
        child_SK = test['child_SK']
        assert derive_child_SK(parent_SK=parent_SK, index=index) == child_SK
