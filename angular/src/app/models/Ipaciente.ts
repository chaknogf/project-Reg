export interface Ipaciente {
  [key: string]: string | number | boolean | Date;
  id: number;
  expediente: number;
  nombre: string;
  apellido: string;
  dpi: number;
  pasaporte: string;
  sexo: string;
  nacimiento: Date;
  nacionalidad: number;
  lugar_nacimiento: number;
  estado_civil: number;
  educacion: number;
  pueblo: number;
  idioma: number;
  ocupacion: string;
  direccion: string;
  telefono: number;
  email: string;
  padre: string;
  madre: string;
  responsable: string;
  parentesco: number;
  dpi_responsable: number;
  telefono_responsable: number;
  estado: string;
  exp_madre: number;
  user: string;
  fechaDefuncion: string | Date;
  municipio: string;
  nation: string;
  people: string;
  ecivil: string;
  academic: string;
  parents: string;
  lenguage: string;

}

