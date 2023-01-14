class Accumulated:
    """create a array with length determined,
    it can to calculate accumuleted in definite range
    """

    def __init__(self, length: int) -> None:
        if not (0 < length and length <= 200):
            raise ValueError('the length N is out range 1 < N < 200')

        values = input().split()
        if len(values) != length:
            raise TabError('amount of elements wrong')
        
        self.array = [int(N) for N in values]
        self.array = [N for N in self.array if N < 1000000 and N > -1000000]
        
        if len(self.array) != length:
            raise ValueError('the array only accept values integers what in',
                'absolute value are not greatest than one million')
    

    def accumulate(self, i: int, j: int) -> int:
        """calculate accumuleted(summation) in the range [i, j]
        it satisfying with 0 ≤ i ≤ j ≤ N-1, N being the array's length
        """
        
        if  type(i) != int or type(j) != int:
            raise ValueError('arguments must be integers')
        if i > j:
            raise ValueError('argument i must be less than or equal to j')
        if i < 0:
            raise IndexError('argument i mustn\'t be less than zero')
        if j > len(self.array) - 1:
            raise IndexError('argument j out range of the array')

        return sum(self.array[i:j+1])
        

def run() -> None:
    print('Ingresa el tamaño N del arreglo(1 ≤ N ≤ 200) y en la siguiente',
        'linea el arreglo separando sus elementos con espacios')
    N = int(input())
    X = Accumulated(N)
    K = int(input('Ingresa el número de consultas:\n'))
    
    answer = list()
    for i in range(K):
        print('Ingresa los indices i y j para hallar el acumulado',
            'entre ellos:')
        query = input().split()
        
        try:
            assert len(query) == 2, 'consulta incorrecta'
        
            try:
                i = int(query[0])
                j = int(query[1])
                answer.append(X.accumulate(i, j))
            except (ValueError, IndexError) as e:
                print(e)

        except AssertionError as e:
            print(e)

    for i in answer:
        print(i)


if __name__ == '__main__':
    run()


from unittest import TestCase, mock
import io


class GlassBoxTest(TestCase):
    # Regression  testing or mocks

    @mock.patch('7_acumulados.input', create=True)
    def test_Accumulated_object(self, mocked_input):
        N = 1
        mocked_input.side_effect = ['1']
        X = Accumulated(N)

        self.assertEqual(type(X), Accumulated)


    def test_N_out_range(self):
        N = 201
        with self.assertRaises(ValueError):
            X = Accumulated(N)


    @mock.patch('7_acumulados.input', create=True)
    def test_array_overflow(self, mocked_input):
        N = 1
        mocked_input.side_effect = ['1 2']
        with self.assertRaises(TabError):
            X = Accumulated(N)


    @mock.patch('7_acumulados.input', create=True)
    def test_elements_out_range(self, mocked_input):
        N = 3
        mocked_input.side_effect = ['1000001 -1000001 1']
        with self.assertRaises(ValueError):
            X = Accumulated(N)


    @mock.patch('7_acumulados.input', create=True)
    def test_accumulate(self, mocked_input):
        N = 3
        mocked_input.side_effect = ['2 3 5']
        X = Accumulated(N)
        i, j = 0, 2
        summation = X.accumulate(i, j)
        self.assertEqual(summation, 10)


    @mock.patch('7_acumulados.input', create=True)
    def test_accumulate_arg_not_int(self, mocked_input):
        N = 3
        mocked_input.side_effect = ['2 3 5']
        X = Accumulated(N)
        i, j = 0, 2.3
        with self.assertRaises(ValueError):
            X.accumulate(i, j)


    @mock.patch('7_acumulados.input', create=True)
    def test_accumulate_arg_j_lower_than_i(self, mocked_input):
        N = 3
        mocked_input.side_effect = ['2 3 5']
        X = Accumulated(N)
        i, j = 2, 0
        with self.assertRaises(ValueError):
            X.accumulate(i, j)


    @mock.patch('7_acumulados.input', create=True)
    def test_accumulate_arg_i_negative(self, mocked_input):
        N = 3
        mocked_input.side_effect = ['2 3 5']
        X = Accumulated(N)
        i, j = -1, 2
        with self.assertRaises(IndexError):
            X.accumulate(i, j)


    @mock.patch('7_acumulados.input', create=True)
    def test_accumulate_arg_j_out_range(self, mocked_input):
        N = 3
        mocked_input.side_effect = ['2 3 5']
        X = Accumulated(N)
        i, j = 0, 3
        with self.assertRaises(IndexError):
            X.accumulate(i, j)


    @mock.patch('7_acumulados.input', create=True)
    def test_N_not_int(self, mocked_input):
        mocked_input.side_effect = ['2.3']
        with self.assertRaises(ValueError):
            run()


    @mock.patch('7_acumulados.input', create=True)
    def test_K_not_int(self, mocked_input):
        mocked_input.side_effect = ['1', '1', 'a']
        with self.assertRaises(ValueError):
            run()


    @mock.patch('7_acumulados.input', create=True)
    def test_query_sintax_wrong(self, mocked_input):
        mocked_input.side_effect = ['1', '1', '1', '1']
        with self.assertRaises(AssertionError):
            run()
