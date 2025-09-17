
"""
Desafio Final – Sistema de Cadastro de Veículos (POO)
Requisitos atendidos:
- Classe base Veiculo com atributos protegidos (marca, modelo, ano), getters/setters e __str__
- Classes derivadas Carro, Moto, Caminhao com atributos próprios e polimorfismo (métodos sobrescritos)
- Função principal para cadastrar diferentes veículos, armazená-los em uma lista e exibir relatório

Como executar:
  python sistema_cadastro_veiculos.py
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Veiculo(ABC):
    def __init__(self, marca: str, modelo: str, ano: int) -> None:
        self._marca = marca.strip()
        self._modelo = modelo.strip()
        self._ano = int(ano)

    @property
    def marca(self) -> str:
        return self._marca

    @marca.setter
    def marca(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("Marca não pode ser vazia.")
        self._marca = valor.strip()

    @property
    def modelo(self) -> str:
        return self._modelo

    @modelo.setter
    def modelo(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("Modelo não pode ser vazio.")
        self._modelo = valor.strip()

    @property
    def ano(self) -> int:
        return self._ano

    @ano.setter
    def ano(self, valor: int) -> None:
        valor = int(valor)
        if valor < 1886:
            raise ValueError("Ano inválido para veículo.")
        self._ano = valor

    @property
    def tipo(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def detalhes(self) -> str:
        raise NotImplementedError

    def __str__(self) -> str:
        return f"{self.tipo}: {self.marca} {self.modelo} ({self.ano}) | {self.detalhes()}"


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, portas: int, combustivel: str) -> None:
        super().__init__(marca, modelo, ano)
        self._portas = int(portas)
        self._combustivel = combustivel.strip()

    def detalhes(self) -> str:
        return f"portas={self._portas}, combustivel={self._combustivel}"


class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cilindradas: int, partida_eletrica: bool) -> None:
        super().__init__(marca, modelo, ano)
        self._cilindradas = int(cilindradas)
        self._partida_eletrica = bool(partida_eletrica)

    def detalhes(self) -> str:
        pe = "sim" if self._partida_eletrica else "não"
        return f"cilindradas={self._cilindradas}cc, partida_eletrica={pe}"


class Caminhao(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, eixos: int, carga_max_kg: float) -> None:
        super().__init__(marca, modelo, ano)
        self._eixos = int(eixos)
        self._carga_max_kg = float(carga_max_kg)

    def detalhes(self) -> str:
        return f"eixos={self._eixos}, carga_max={self._carga_max_kg:.0f}kg"


def cadastrar_veiculo() -> Veiculo | None:
    print("\n=== Novo Veículo ===")
    print("1) Carro  |  2) Moto  |  3) Caminhão  |  0) Cancelar")
    tipo = input("Escolha o tipo: ").strip()

    if tipo == "0":
        return None

    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()
    ano = int(input("Ano: "))

    if tipo == "1":
        portas = int(input("Portas: "))
        combustivel = input("Combustível: ").strip()
        return Carro(marca, modelo, ano, portas, combustivel)

    elif tipo == "2":
        cilindradas = int(input("Cilindradas (cc): "))
        partida_eletrica = input("Partida elétrica? (s/n): ").strip().lower() == "s"
        return Moto(marca, modelo, ano, cilindradas, partida_eletrica)

    elif tipo == "3":
        eixos = int(input("Número de eixos: "))
        carga_max_kg = float(input("Carga máxima (kg): "))
        return Caminhao(marca, modelo, ano, eixos, carga_max_kg)

    else:
        print("❌ Tipo inválido.")
        return None


def exibir_relatorio(veiculos: List[Veiculo]) -> None:
    print("\n=== Relatório de Veículos Cadastrados ===")
    if not veiculos:
        print("(vazio)")
        return

    print(f"{'#':<3} {'Tipo':<10} {'Marca':<15} {'Modelo':<18} {'Ano':<6} Detalhes")
    print("-" * 70)
    for i, v in enumerate(veiculos, 1):
        print(f"{i:<3} {v.tipo:<10} {v.marca:<15} {v.modelo:<18} {v.ano:<6} {v.detalhes()}")


def main() -> None:
    veiculos: List[Veiculo] = []

    while True:
        print("\n=== Menu ===")
        print("1) Cadastrar veículo")
        print("2) Exibir relatório")
        print("0) Sair")
        op = input("Escolha: ").strip()

        if op == "1":
            v = cadastrar_veiculo()
            if v is not None:
                veiculos.append(v)
                print("✅ Veículo cadastrado!")
        elif op == "2":
            exibir_relatorio(veiculos)
        elif op == "0":
            print("Até mais! 👋")
            break
        else:
            print("❌ Opção inválida.")


if __name__ == "__main__":
    main()
