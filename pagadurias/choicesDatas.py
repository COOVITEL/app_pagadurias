FECHAENVIOCUENTAS = [(f"{num}", f"{num}") for num in range(0, 31)]


VISACION = [
  ('Si', 'Si'),
  ('No', 'No'),
]

MEDIOVISACION = [
  ('Correo', 'Correo'),
  ('Fisico', 'Fisico'),
]

ESTADO_CHOICES = [
    ('Por aprobar', 'Por aprobar'),
    ('Aprobado', 'Aprobado'),
    ('Rechazado', 'Rechazado'),
]
TIPOS_EMPRESA = [
    ('Pública', 'Pública'),
    ('Descentralizada', 'Descentralizada'),
    ('Privada', 'Privada'),
    ('Sin ánimo de lucro', 'Sin ánimo de lucro'),
]

PAISES = [
  ('Colombia', 'Colombia'),
  ('Ecuador', 'Ecuador'),
  ('Peru', 'Peru'),
  ('Bolivia', 'Bolivia'),
]

DEPARTAMENTOS = [
  "Amazonas",
  "Antioquia",
  "Arauca",
  "Atlántico",
  "Bolívar",
  "Boyacá",
  "Caldas",
  "Caquetá",
  "Casanare",
  "Cauca",
  "Cesar",
  "Chocó",
  "Córdoba",
  "Cundinamarca",
  "Guainía",
  "Guaviare",
  "Huila",
  "La Guajira",
  "Magdalena",
  "Meta",
  "Nariño",
  "Norte de Santander",
  "Putumayo",
  "Quindío",
  "Risaralda",
  "San Andrés y Providencia",
  "Santander",
  "Sucre",
  "Tolima",
  "Valle del Cauca",
  "Vaupés",
  "Vichada"
]

CIUDADES = {
  "Amazonas": ["Leticia", "Puerto Nariño"],
  "Antioquia": ["Medellín", "Bello", "Itagüí", "Envigado", "Apartadó"],
  "Arauca": ["Arauca", "Saravena", "Tame"],
  "Atlántico": ["Barranquilla", "Soledad", "Malambo", "Sabanalarga"],
  "Bolívar": ["Cartagena", "Magangué", "Turbaco"],
  "Boyacá": ["Tunja", "Duitama", "Sogamoso", "Chiquinquirá"],
  "Caldas": ["Manizales", "La Dorada", "Chinchiná"],
  "Caquetá": ["Florencia", "San Vicente del Caguán", "Puerto Rico"],
  "Casanare": ["Yopal", "Aguazul", "Villanueva"],
  "Cauca": ["Popayán", "Santander de Quilichao", "Puerto Tejada"],
  "Cesar": ["Valledupar", "Aguachica", "La Jagua de Ibirico"],
  "Chocó": ["Quibdó", "Istmina", "Riosucio"],
  "Córdoba": ["Montería", "Lorica", "Sahagún"],
  "Cundinamarca": ["Bogotá", "Soacha", "Zipaquirá", "Girardot", "Facatativá"],
  "Guainía": ["Inírida"],
  "Guaviare": ["San José del Guaviare", "Calamar"],
  "Huila": ["Neiva", "Pitalito", "Garzón"],
  "La Guajira": ["Riohacha", "Maicao", "Fonseca"],
  "Magdalena": ["Santa Marta", "Ciénaga", "Fundación"],
  "Meta": ["Villavicencio", "Acacías", "Granada"],
  "Nariño": ["Pasto", "Tumaco", "Ipiales"],
  "Norte de Santander": ["Cúcuta", "Ocaña", "Pamplona"],
  "Putumayo": ["Mocoa", "Puerto Asís", "Orito"],
  "Quindío": ["Armenia", "Calarcá", "Montenegro"],
  "Risaralda": ["Pereira", "Dosquebradas", "Santa Rosa de Cabal"],
  "San Andrés y Providencia": ["San Andrés", "Providencia"],
  "Santander": ["Bucaramanga", "Floridablanca", "Girón", "Barrancabermeja"],
  "Sucre": ["Sincelejo", "Corozal", "San Marcos"],
  "Tolima": ["Ibagué", "Espinal", "Honda"],
  "Valle del Cauca": ["Cali", "Palmira", "Buenaventura", "Tuluá"],
  "Vaupés": ["Mitú"],
  "Vichada": ["Puerto Carreño"]
}