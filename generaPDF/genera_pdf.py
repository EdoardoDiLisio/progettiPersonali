from fpdf import FPDF

# Classe personalizzata per il PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Progetto TuTubi - Documentazione Completa', border=False, ln=True, align='C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, border=False, ln=True, align='L')
        self.ln(5)
Quale istruzione SQL permette di definire il tipo di dato enumerativo Genere con valori ‘M’ ed ‘F’?

￼￼Question 7Answer
￼
CREATE DOMAIN Genere AS [‘M’, ‘F’];

￼
CREATE TYPE Genere AS [‘M’, ‘F’];

￼
CREATE TYPE Genere AS ENUM (‘M’, ‘F’);

￼
CREATE DOMAIN Genere AS ENUM (‘M’, ‘F’);f, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

# Creazione del PDF
pdf = PDF()
pdf.add_page()

# Sezione 1: Introduzione
pdf.chapter_title("1. Introduzione")
intro_text = (
    "Il progetto TuTubi prevede la realizzazione di un sistema per la condivisione e "
    "gestione di video tramite un portale web. Gli utenti possono caricare, visualizzare, "
    "valutare e commentare video, oltre a creare playlist personalizzate. "
    "La redazione ha la facoltà di moderare i contenuti."
)
pdf.chapter_body(intro_text)

# Sezione 2: Casi d'Uso
pdf.chapter_title("2. Diagramma degli Use Case")
use_case_description = (
    "Il diagramma degli Use Case rappresenta le interazioni tra:\n"
    "- Utente: Può registrarsi, accedere, caricare video, visualizzare, commentare e votare.\n"
    "- Redazione: Può censurare i video.\n"
    "- Sistema: Esegue le operazioni di backend.\n\n"
    "Principali casi d'uso:\n"
    "1. Registrazione e Login\n"
    "2. Caricamento di Video\n"
    "3. Visualizzazione di Video\n"
    "4. Valutazione e Commenti\n"
    "5. Creazione di Playlist\n"
    "6. Ricerca Video\n"
    "7. Moderazione dei Contenuti\n"
)Quale istruzione SQL permette di definire il tipo di dato enumerativo Genere con valori ‘M’ ed ‘F’?

￼￼Question 7Answer
￼
CREATE DOMAIN Genere AS [‘M’, ‘F’];

￼
CREATE TYPE Genere AS [‘M’, ‘F’];

￼
CREATE TYPE Genere AS ENUM (‘M’, ‘F’);

￼
CREATE DOMAIN Genere AS ENUM (‘M’, ‘F’);_description)

# Sezione 3: Specifiche dei Casi d'Uso
pdf.chapter_title("3. Specifiche dei Casi d'Uso")
use_case_specs = (
    "1. Registrazione e Login: Consente agli utenti di accedere alle funzionalità del sistema.\n"
    "2. Pubblicazione Video: Gli utenti possono caricare video con titolo, descrizione, tag e categoria.\n"
    "3. Visione Video: Gli utenti possono visualizzare video e aggiornarne la cronologia.\n"
    "4. Valutazione e Commenti: Gli utenti possono valutare e commentare video, rispettando regole specifiche.\n"
    "5. Playlist: Creazione, gestione e condivisione di playlist pubbliche o private.\n"
    "6. Moderazione: La redazione può censurare contenuti non conformi."
)
pdf.chapter_body(use_case_specs)

# Sezione 4: Diagramma delle Classi (Descrizione)
pdf.chapter_title("4. Diagramma delle Classi")
class_diagram_description = (
    "Il diagramma delle classi include le seguenti entità principali:\n"
    "- Utente: Attributi come id, nome e data di registrazione.\n"
    "- Video: Attributi come titolo, durata, descrizione, categoria e tag.\n"
    "- Playlist: Collezione di video che può essere pubblica o privata.\n"
    "- Valutazione: Associata a un video e un utente, include il punteggio dato.\n"
    "- Commento: Include testo, data e utente associato.\n\n"
    "Le relazioni principali includono:\n"
    "1. Un utente può avere molti video.\n"
    "2. Un video può avere molti commenti e valutazioni.\n"
    "3. Una playlist può contenere molti video."
)
pdf.chapter_body(class_diagram_description)

# Sezione 5: Diagramma delle Sequenze (Descrizione)
pdf.chapter_title("5. Diagramma delle Sequenze")
sequence_text = (
    "Un esempio di diagramma delle sequenze rappresenta il flusso per la pubblicazione di un video:\n"
    "1. L'utente carica il video fornendo titolo, descrizione, tag e categoria.\n"
    "2. Il sistema valida i dati e salva il video nel database.\n"
    "3. Il video diventa disponibile per altri utenti.\n"
    "Analogamente, altri casi d'uso come la valutazione e la ricerca seguono un flusso simile."
)
pdf.chapter_body(sequence_text)

# Sezione 6: Conclusioni
pdf.chapter_title("6. Conclusioni")
conclusion_text = (
    "Il progetto TuTubi offre una piattaforma versatile per la condivisione di video, "
    "con funzionalità avanzate di ricerca, valutazione e gestione dei contenuti. "
    "La struttura modulare del sistema garantisce scalabilità e facilità di manutenzione."
)
pdf.chapter_body(conclusion_text)

# Salvataggio del PDF
output_path = "Progetto_TuTubi_Completo.pdf"
pdf.output(output_path)

print(f"PDF generato con successo: {output_path}")
