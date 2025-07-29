import pickle

try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("✅ Pickle loaded successfully.")
    print("📦 Model object:", type(model))
except Exception as e:
    print("❌ Failed to load pickle:", e)
