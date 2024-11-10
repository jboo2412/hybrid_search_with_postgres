"""
    This module contains SQLAlchemy model for the product data model.
"""

# pylint:disable=missing-class-docstring,missing-function-docstring

from __future__ import annotations
import datetime

from pgvector.sqlalchemy import Vector
from sqlalchemy import Index
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ARRAY,
    Text,
)

from models.database import engine
from models import Base

class Product(Base):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True)
    nom = Column(Text, nullable=False)
    description = Column(Text)
    categorie = Column(Text)
    prix = Column(Numeric)
    sourceImage = Column(Text)
    longueur = Column(Numeric)
    largeur = Column(Numeric)
    hauteur = Column(Numeric)
    unite = Column(Text)
    poids = Column(Text)
    materiau = Column(Text)
    couleur = Column(Text)
    marque = Column(Text)
    stock = Column(Integer)
    disponibilite = Column(Text)
    livraisonEstimee = Column(Text)
    garantie = Column(Text)
    produitsAssocies = Column(ARRAY(Integer))
    tags = Column(ARRAY(Text))
    designer = Column(Text)
    embedding = Column(Vector(1536))
    content = Column(Text)
    created_at= Column(DateTime, default=datetime.datetime.utcnow)

    def to_str(self):
        res = f"Produit: {self.nom}\n"
        res += f"Description: {self.description}\n"
        res += f"Catégorie: {self.categorie}\n"
        res += f"Prix: {self.prix} €\n"
        res += f"Dimensions (L x l x h): {self.longueur} x {self.largeur} x {self.hauteur} {self.unite}\n"
        res += f"Poids: {self.poids}\n"
        res += f"Matériau: {self.materiau}\n"
        res += f"Couleur: {self.couleur}\n"
        res += f"Marque: {self.marque}\n"
        res += f"Stock: {self.stock}\n"
        res += f"Disponibilité: {self.disponibilite}\n"
        res += f"Livraison Estimée: {self.livraisonEstimee}\n"
        res += f"Garantie: {self.garantie}\n"
        res += f"Designer: {self.designer}\n"
        res += f"Tags: {', '.join(self.tags) if self.tags else ''}\n"
        res += f"Produits Associés: {', '.join(map(str, self.produitsAssocies)) if self.produitsAssocies else ''}\n"
        return res
    
    def to_dict(self):
        return {
           "id": self.id,
            "nom": self.nom,
            "description": self.description,
            "categorie": self.categorie,
            "prix": self.prix,
            "sourceImage": self.sourceImage,
            "dimensions": {
                "longueur": self.longueur,
                "largeur": self.largeur,
                "hauteur": self.hauteur,
                "unite": self.unite,
            },
            "poids": self.poids,
            "materiau": self.materiau,
            "couleur": self.couleur,
            "marque": self.marque,
            "stock": self.stock,
            "disponibilite": self.disponibilite,
            "livraisonEstimee": self.livraisonEstimee,
            "garantie": self.garantie,
            "produitsAssocies": self.produitsAssocies,
            "tags": self.tags,
            "designer": self.designer
        }

    @staticmethod
    def get_text_search_field():
        return "content"

    @staticmethod
    def get_embedding_field():
        return "embedding"

index_ada002 = Index(
    "hnsw_index_for_innerproduct_product_embedding_ada002",
    Product.embedding,
    postgresql_using="hnsw",
    postgresql_with={"m": 16, "ef_construction": 64},
    postgresql_ops={"embedding_ada002": "vector_ip_ops"},
)

Base.metadata.create_all(engine)
