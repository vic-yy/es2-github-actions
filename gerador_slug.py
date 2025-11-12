# gerador_slug.py
import re
import unicodedata

def slugify(texto: str) -> str:
    """
    Converte um texto em um "slug" amigável para URLs.
    - Remove acentos
    - Converte para minúsculas
    - Remove caracteres especiais (deixa letras, números e hífens)
    - Substitui espaços por hífens
    - Remove hífens duplicados ou no início/fim
    """
    if not texto:
        return ""

    # 1. Normalizar e remover acentos (ex: "ç" -> "c")
    # Transforma em "Formato de Decomposição de Compatibilidade" e remove
    # caracteres não-ASCII (os acentos)
    texto_normalizado = (
        unicodedata.normalize("NFKD", texto)
        .encode("ascii", "ignore")
        .decode("utf-8")
    )

    # 2. Converter para minúsculas
    texto = texto_normalizado.lower()

    # 3. Remover caracteres especiais (manter letras, números, espaços e hífens)
    texto = re.sub(r"[^a-z0-9\s-]", "", texto)

    # 4. Substituir espaços por hífens
    texto = re.sub(r"[\s]+", "-", texto)

    # 5. Remover hífens duplicados
    texto = re.sub(r"[-]+", "-", texto)

    # 6. Remover hífens no início ou fim
    texto = texto.strip("-")

    return texto