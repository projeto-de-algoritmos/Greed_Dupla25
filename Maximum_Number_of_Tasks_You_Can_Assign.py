from typing import List
import bisect

# A resposta comeca aqui

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
    #def maxTaskAssign(tasks: List[int], workers: List[int], pills: int, strength: int) -> int:

        # Ordenando os vertores tasks e workers
            tasks = sorted(tasks)
            workers = sorted(workers)
        # Definindo o inicio e o fim para a busca binaria
            inicio = 0
            fim = min(len(tasks), len(workers))
        # O boolean diz se muda o inicio(True) ou fim(False)
            boolean = True

            # Comeca a busca binaria
            while inicio <= fim:
                
            # Definindo o meio para a busca binaria
                meio = int(inicio + (fim-inicio)/2)
            # t_aux copia taskers da posicao 0 ate meio
                t_aux=tasks[:meio]
            # w_aux copia workers da posicao meio ate o final
                w_aux=workers[len(workers)-meio:]
                
                p_aux=pills
                s_aux=strength
            # Pega a posicao do trabalhador mais forte
                strongest = -1
            # Pega a posicao do tarefa mais dificil
                harder = len(t_aux) - 1

                for x in range(len(t_aux)):
                # Se o worker mais forte for maior ou igual a task mais dificil
                    if w_aux[strongest] >= t_aux[harder]:
                    # Tira o worker mais forte
                        w_aux.pop()

                    else:
                    # Se nao tem pilulas ira mudar o fim da busca binaria
                        if not p_aux: 
                            boolean = False
                            break

                        forca_necessaria = t_aux[harder] - s_aux
                    # Pega a posicao mais a esquerda com o valor correspondente a forca_necessaria
                        index = bisect.bisect_left(w_aux,forca_necessaria)

                    # Se o index for maior ou igual ao tamanho de w_aux
                        if index >= len(w_aux): 
                            boolean = False
                            break
                    # Diminui a quantidade de pulilas
                        p_aux -= 1
                        w_aux.pop(index)
                    # Pega a posicao do proxima task mais dificil
                    harder -=  1
            
            # atualiza inicio
                if boolean:
                    inicio = meio + 1
            # atualiza fim
                else:
                    fim = meio - 1
                boolean = True
            
            return fim

# A resposta termina aqui


if __name__ == '__main__':
    tasks=[5,9,8,5,9]
    workers=[1,6,4,2,6]
    pills=1
    strength=5
    x=Solution
    print(x.maxTaskAssign(x, tasks, workers, pills, strength))

    
