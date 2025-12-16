import streamlit as st
# Dodaję emotikonę Mikołaja (🎅) do tytułu okna przeglądarki i Streamlit.
# Należy to zrobić przy pomocy funkcji st.set_page_config() na samym początku.
st.set_page_config(page_title="Magazyn Mikołaja", page_icon="🎅")

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

# --- Główna Aplikacja Streamlit (POPRAWIONA) ---

def main():
    # Zmiana tytułu - dodanie Mikołaja i świątecznego akcentu
    st.title("🎅✨ Magazyn Mikołaja - Świąteczna Edycja")
    st.markdown("---")

    # 1. Inicjalizacja Magazynu w Session State
    if 'magazyn' not in st.session_state:
        st.session_state.magazyn = [] 

    st.header("➕ Dodaj Produkt (Prezent)")
    
    nowy_produkt = st.text_input("Wpisz nazwę prezentu:", key="input_dodaj")
    
    # POPRAWKA 1: Dodanie unikalnego klucza (key) do przycisku dodawania
    if st.button("Dodaj do Magazynu Prezentów", key="btn_dodaj"):
        dodaj_produkt(nowy_produkt.strip())
        
    st.markdown("---")

    # 2. Wyświetlanie Zawartości Magazynu
    st.header("🎁 Aktualna Lista Prezentów w Worku")
    
    if st.session_state.magazyn:
        posortowany_magazyn = sorted(st.session_state.magazyn)
        
        st.code('\n'.join(posortowany_magazyn), language='text')

        st.markdown("---")
        
        # 3. Usuwanie Produktu
        st.header("🗑️ Usuń Produkt (Zepsuty lub Niegrzeczny)")
        
        opcje_usun = ["-- Wybierz --"] + posortowany_magazyn
        
        produkt_do_usunięcia = st.selectbox(
            "Wybierz prezent do usunięcia:", 
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
        st.info("🎁 Worek Mikołaja jest pusty! Czas zacząć produkcję!")

# Uruchomienie głównej funkcji
if __name__ == "__main__":
    main()
