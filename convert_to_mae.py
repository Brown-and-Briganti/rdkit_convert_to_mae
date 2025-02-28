from pathlib import Path
from rdkit import Chem
from rdkit.Chem import SDMolSupplier
from rdkit.Chem.rdmolfiles import MaeWriter


def sdf_to_one_mae():
    for sdf in sdf_paths:
        output_file = output_dir / (Path(sdf).stem + ".mae")
        suppl = SDMolSupplier(sdf, removeHs=False)
        with MaeWriter(output_file) as writer:
            for mol in suppl:
                if mol is not None:
                    for atom in mol.GetAtoms():
                        symbol = atom.GetSymbol()
                        atom_name = symbol.rjust(4)
                        atom.SetProp("s_m_pdb_atom_name", atom_name)
                    writer.write(mol)


def pdb_to_one_mae():
    for pdb in pdb_paths:
        output_file = output_dir / (Path(pdb).stem + ".mae")

        with open(pdb, 'r') as file:
            pdb_content = file.read()

        models = pdb_content.split("MODEL")

        with MaeWriter(output_file) as writer:
            for idx, model in enumerate(models):
                if model.strip():
                    pdb_block = "MODEL" + model

                    mol = Chem.MolFromPDBBlock(pdb_block, sanitize=False, removeHs=False)

                    if mol is not None:
                        for atom in mol.GetAtoms():
                            symbol = atom.GetSymbol()
                            atom_name = symbol.rjust(4)
                            atom.SetProp("s_m_pdb_atom_name", atom_name)
                        writer.write(mol)


input_dir = Path("./inputs")
output_dir = Path("./outputs")
output_dir.mkdir(parents=True, exist_ok=True)


sdf_paths = [file for file in input_dir.glob("*.*") if file.suffix.lower() == ".sdf"]
pdb_paths = [file for file in input_dir.glob("*.*") if file.suffix.lower() == ".pdb"]

if len(sdf_paths) > 0:
    sdf_to_one_mae()

if len(pdb_paths) > 0:
    pdb_to_one_mae()