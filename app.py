import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM

st.set_page_config(page_title="IA Assistant de Cours", layout="wide")
st.title("📚 Assistant IA : Résumé & Concepts de Cours")

# 1. Chargement de la base de données et du modèle LLM
@st.cache_resource
def init_models():
    # Chargement de la base vectorielle
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local("vector_db", embedding_model, allow_dangerous_deserialization=True)
    
    # Connexion à Llama 3 via Ollama
    llm = OllamaLLM(model="llama3", temperature=0.3)
    return db, llm

try:
    db, llm = init_models()
    st.success("✅ L'IA et ton cours sont prêts !")
except Exception as e:
    st.error(f"❌ Erreur de configuration : {e}")

# 2. Interface utilisateur Streamlit
st.subheader("Que veux-tu que je t'explique ou résume aujourd'hui ?")
question = st.text_input(
    "Exemple : 'Fais-moi un résumé du chapitre 1' ou 'Explique-moi le concept de...'",
    placeholder="Écris ta demande ici..."
)

if question:
    with st.spinner("🧠 L'IA analyse ton cours et rédige la réponse..."):
        try:
            # Étape 1 : Récupérer directement les pages du cours (FAISS pur)
            docs = db.similarity_search(question, k=4)
            
            # Étape 2 : Fusionner les textes trouvés pour créer le contexte
            contexte = "\n\n".join([doc.page_content for doc in docs])
            
            # Étape 3 : Créer une consigne simple (Prompt) en texte brut
            prompt = f"""Tu es un assistant pédagogique expert. Rédige un résumé clair, structuré et détaillé en français en te basant uniquement sur les extraits du cours fournis ci-dessous.

Extraits du cours :
{contexte}

Demande de l'étudiant : {question}
Réponse en français :"""

            # Étape 4 : Envoyer directement le texte à Ollama
            reponse = llm.invoke(prompt)
            
            st.subheader("📝 Résumé / Explication de l'IA :")
            st.write(reponse)
            
        except Exception as e:
            st.error(f"Une erreur est survenue lors de la génération : {e}")