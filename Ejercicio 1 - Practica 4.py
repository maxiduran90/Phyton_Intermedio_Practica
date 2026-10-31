from abc import ABC, abstractmethod

class CuentaBancaria(ABC):
    def __init__(self, titular: str, cbu: str, saldo_inicial: float = 0.0):
        self.titular = titular          # Atributo Público
        self._cbu = cbu                 # Atributo Protegido
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser menor a cero.")
        self._saldo = saldo_inicial     # Atributo Protegido

    @property
    def cbu(self) -> str:
        """Propiedad de solo lectura para el CBU."""
        return self._cbu

    @property
    def saldo(self) -> float:
        """Propiedad para leer el saldo."""
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo: float):
        """Setter que valida que el saldo no sea menor a cero."""
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser menor a cero.")
        self._saldo = nuevo_saldo

    def depositar(self, monto: float):
        """Suma dinero validando que el monto sea mayor a 0."""
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a cero.")
        self.saldo += monto

    @abstractmethod
    def extraer(self, monto: float):
        """Método abstracto obligatorio sin cuerpo."""
        pass

    def __str__(self) -> str:
        # Se obtiene el nombre de la clase dinámica para [TIPODECUENTA]
        tipo_cuenta = self.__class__.__name__
        return f"[{tipo_cuenta}] Titular: {self.titular} | CBU: {self.cbu} | Saldo: ${self.saldo:.2f}"


class CuentaAhorro(CuentaBancaria):
    def extraer(self, monto: float):
        """Permite retirar únicamente si monto <= saldo."""
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor a cero.")
        if monto > self.saldo:
            print(f"Fondos insuficientes en Cuenta Ahorro. Saldo actual: ${self.saldo}")
            return
        self.saldo -= monto

    def aplicar_interes(self):
        """Suma al saldo un interés del 0.1% (tasa = 0.001)."""
        interes = self.saldo * 0.001
        self.saldo += interes


class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular: str, cbu: str, saldo_inicial: float = 0.0, limite_descubierto: float = 500.0):
        super().__init__(titular, cbu, saldo_inicial)
        self.limite_descubierto = limite_descubierto

    def extraer(self, monto: float):
        """Permite retirar dinero si no supera saldo + limite_descubierto."""
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor a cero.")
        limite_maximo = self.saldo + self.limite_descubierto
        if monto > limite_maximo:
            print(f"Límite de descubierto excedido. Máximo permitido retirar: ${limite_maximo}")
            return
        # Modifica directamente la variable protegida para permitir saldo negativo temporal dentro del descubierto
        nuevo_saldo = self._saldo - monto
        if nuevo_saldo < -self.limite_descubierto:
            raise ValueError("El saldo supera el límite de descubierto permitido.")
        self._saldo = nuevo_saldo


class CuentaCheque(CuentaBancaria):
    def __init__(self, titular: str, cbu: str, saldo_inicial: float = 0.0, costo_emision: float = 50.0):
        super().__init__(titular, cbu, saldo_inicial)
        self.costo_emision = costo_emision

    def extraer(self, monto: float):
        """Descuenta el monto solicitado más el costo administrativo por emisión."""
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor a cero.")
        total_a_descontar = monto + self.costo_emision
        if total_a_descontar > self.saldo:
            print(f"Fondos insuficientes para cubrir la extracción y el costo de emisión (${self.costo_emision}).")
            return
        self.saldo -= total_a_descontar


# --- DEMOSTRACIÓN DE USO ---
if __name__ == "__main__":
    print("--- Probando Cuenta Ahorro ---")
    ca = CuentaAhorro("Ana Gómez", "123456789", 1000.0)
    print(ca)
    ca.depositar(500)
    ca.aplicar_interes()
    print("Luego de depósito e interés:", ca)
    ca.extraer(300)
    print("Luego de extraer $300:", ca)
    ca.extraer(2000) # Intento de extracción mayor al saldo
    
    print("\n--- Probando Cuenta Corriente ---")
    cc = CuentaCorriente("Carlos Pérez", "987654321", 200.0, 500.0)
    print(cc)
    cc.extraer(600) # Usa $400 del descubierto
    print("Luego de extraer $600 (usando descubierto):", cc)
    cc.extraer(200) # Intenta exceder el descubierto total

    print("\n--- Probando Cuenta Cheque ---")
    ch = CuentaCheque("Juan López", "456789123", 500.0, 50.0)
    print(ch)
    ch.extraer(200) # Debe descontar 200 + 50 = 250
    print("Luego de extraer $200 (más $50 de comisión):", ch)
