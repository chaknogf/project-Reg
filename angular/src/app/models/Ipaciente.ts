export interface Ipaciente {
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
  idioma: string;
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
  user: string;
}
