#Con py3Dmol y rdkit. Crear el modelo 3d de las siguientes moleculas con su notación SMILE

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

# SMILES válido para el agua
smiles = "O"
nombre = "Agua (H2O)"

# Generación de la molécula
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)  # Agregar hidrógenos explícitos
AllChem.EmbedMolecule(mol, AllChem.ETKDG())  # Generar la geometría 3D
mb = Chem.MolToMolBlock(mol)

# Visualización con py3Dmol
viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

# Guardar el modelo en un archivo HTML
output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CCO"
nombre = "Etanol"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C1CCCCC1"
nombre = "Ciclohexano"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CC(=O)O"
nombre = "Ácido acético"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C1=CC=CC=C1"
nombre = "Benceno"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C"
nombre = "Metano"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CO"
nombre = "Metanol"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CC"
nombre = "Etano"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CCC"
nombre = "Propano"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CCCC"
nombre = "Butano"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CC(C=O)C"
nombre = "Acetona"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C(C(=O)O)N"
nombre = "Glicina"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CC(C(=O)O)N"
nombre = "Alanina"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C1=CC=C(C=C1)O"
nombre = "Fenol"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C1CCOCC1"
nombre = "Tetrahidrofurano"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "NCCO"
nombre = "Etanolamina"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C(C(=O)O)(N)C(=O)O"
nombre = "Ácido aspártico"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CCN(CC)CC"
nombre = "Trietilamina"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CCOCC"
nombre = "Dietil éter"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C(C(=O)O)O"
nombre = "Ácido láctico"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C1=CC=C2C=CC=CC2=C1"
nombre = "Naftaleno"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CN(C)C=O"
nombre = "Dimetilformamida"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C(C(=O)O)(C(=O)O)O"
nombre = "Ácido cítrico"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
mb = Chem.MolToMolBlock(mol)

viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(mb, "mol")
viewer.setStyle({"stick": {}})
viewer.setBackgroundColor("white")
viewer.zoomTo()

output_file = f"{nombre.replace(' ', '_')}.html"
with open(output_file, "w") as f:
    f.write(viewer._make_html())
print(f"Modelo 3D guardado en:{output_file}")
