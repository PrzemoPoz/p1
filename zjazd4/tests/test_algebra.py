import zjazd4.mathematica.algebra.matrices as mat
import pytest

def test_add_matrices1():
    mat1=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    mat2=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    assert mat.add_matrices(mat1,mat2)==[
    [2,4,6],
    [8,10,12],
    [14,16,18]
    ]

def test_add_matrices2():
    mat1=[
    [4,5,6],
    [7,8,9]
    ]
    mat2=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    with pytest.raises(ValueError) as e:
        mat.add_matrices(mat1,mat2)

def test_sub_matrices1():
    mat1=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    mat2=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    assert mat.sub_matrices(mat1,mat2)==[
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]

def test_sub_matrices2():
    mat1=[
    [4,5,6],
    [7,8,9]
    ]
    mat2=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    with pytest.raises(ValueError) as e:
        mat.add_matrices(mat1,mat2)
