import streamlit as st

# --- Funkcje Logiki Magazynowej (BEZ ZMIAN) ---

def dodaj_produkt(nazwa_produktu):
    """Dodaje produkt do magazynu (listy w state sesji)."""
    if nazwa_produktu and nazwa_produktu not in st.session_state.magazyn:
        st.session_state.magazyn.append(nazwa_produktu)
        st.success(f"Dodano produkt: **{nazwa_produktu}**")
    elif nazwa_produktu in st.session_state.magazyn:
        st.warning(f"Produkt **{nazwa_produktu}** jest już w magazynie.")
    else:
        st.error("Nazwa produktu nie może być pusta.")

def usun_produkt(nazwa_produktu):
    """Usuwa produkt z magazynu."""
    if nazwa_produktu in st.session_state.magazyn:
        st.session_state.magazyn.remove(nazwa_produktu)
        st.success(f"Usunięto produkt: **{nazwa_produktu}**")
    # Poniższe else nie jest potrzebne w tej logice, bo produkt zawsze jest z selectboxa
    # else:
    #     st.warning(f"Produkt **{nazwa_produktu}** nie został znaleziony w magazynie.")

# --- Główna Aplikacja Streamlit (POPRAWIONA) ---

def main():
    st.title("📦 Prosta Aplikacja Magazynowa")
    st.markdown("---")

    # 1. Inicjalizacja Magazynu w Session State
    if 'magazyn' not in st.session_state:
        st.session_state.magazyn = [] 

    st.header("➕ Dodaj Produkt")
    
    nowy_produkt = st.text_input("Wpisz nazwę produktu:", key="input_dodaj")
    
    # POPRAWKA 1: Dodanie unikalnego klucza (key) do przycisku dodawania
    if st.button("Dodaj do Magazynu", key="btn_dodaj"):
        dodaj_produkt(nowy_produkt.strip())
        
    st.markdown("---")

    # 2. Wyświetlanie Zawartości Magazynu
    st.header("Aktualna Zawartość Magazynu")
    
    if st.session_state.magazyn:
        posortowany_magazyn = sorted(st.session_state.magazyn)
        
        st.code('\n'.join(posortowany_magazyn), language='text')

        st.markdown("---")
        
        # 3. Usuwanie Produktu
        st.header("➖ Usuń Produkt")
        
        # Opcje do selectboxa
        opcje_usun = ["-- Wybierz --"] + posortowany_magazyn
        
        produkt_do_usunięcia = st.selectbox(
            "Wybierz produkt do usunięcia:", 
            options=opcje_usun,
            key="select_usun"
        )
        
        # POPRAWKA 2: Użycie JEDNEGO przycisku z unikalnym kluczem
        if st.button("Usuń z Magazynu", key="btn_usun"):
            if produkt_do_usunięcia != "-- Wybierz --":
                usun_produkt(produkt_do_usunięcia)
            else:
                st.warning("Musisz wybrać produkt do usunięcia.")

    else:
        st.info("Magazyn jest obecnie pusty.")

# Uruchomienie głównej funkcji
if __name__ == "__main__":
    main()
