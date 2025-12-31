class LimpaCPF:
    
    def fix(cpf: str) -> str:
        return cpf.replace(".", "").replace("-", "").strip()
