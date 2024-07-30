import pickle
f = open ('arquivoBinario.pkl','rb')
e = pickle.load(f)
print(e)