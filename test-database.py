import database


def test_load_1():
    i_1=0
    i_2=1
    r_1=database.load(i_1)
    r_2=database.load(i_2)
    assert(r_1.shape[1]==r_2.shape[1]==12)
