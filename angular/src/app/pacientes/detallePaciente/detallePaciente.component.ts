
// import { interval } from 'rxjs';
import { PacientesService } from './../../services/pacientes.service';
import { Component, OnInit, HostBinding } from '@angular/core';
import { Ipaciente } from 'src/app/models/ipaciente';
import { ActivatedRoute, Router } from '@angular/router';
import { FormGroup, FormBuilder } from '@angular/forms';
import { jsPDF } from 'jspdf';


@Component({
  selector: 'detallePaciente',
  templateUrl: './detallePaciente.component.html',
  styleUrls: ['./detallePaciente.component.css']
})
export class DetallePacienteComponent implements OnInit {

  @HostBinding('class') clases = 'row';

  // // Objeto del paciente
  p: Ipaciente = {
    id: 0,
    expediente: 0,
    nombre: "",
    apellido: "",
    dpi: 0,
    pasaporte: "",
    sexo: "M",
    nacimiento: new Date(),
    nacionalidad: 1,
    lugar_nacimiento: 0,
    estado_civil: 0,
    educacion: 0,
    pueblo: 0,
    idioma: 0,
    ocupacion: "",
    direccion: "",
    telefono: 0,
    email: "user@example.com",
    padre: "",
    madre: "",
    responsable: "",
    parentesco: 0,
    dpi_responsable: 0,
    telefono_responsable: 0,
    estado: "v",
    exp_madre: 0,
    user: "admin",
    fechaDefuncion: "",  // Variable para la fecha de defunción
    municipio: "",
    nation: "",
    people: "",
    ecivil: "",
    academic: "",
    parents: "",
    lenguage: ""

  };

  view: boolean = false;
  vistaActual: string;


  constructor(public PacientesService: PacientesService, private router: Router, private activateRoute: ActivatedRoute, private formBuilder: FormBuilder) {
 // Establecer la vista por defecto
    this.vistaActual = 'vista1';
  }

  cambiarVista(vista: string) {
    this.vistaActual = vista;
  }


  generarPDF() {
    // Lógica para generar el documento PDF
    const doc = new jsPDF();
    doc.text('Contenido del PDF', 10, 10);
    doc.save('documento.pdf');
  }


  ngOnInit() {

    // Obtener los parámetros de la ruta
    const params = this.activateRoute.snapshot.params;

    // Verificar si se proporcionó un ID de paciente
    if (params['id']) {
      this.PacientesService.getPaciente(params['id'])
        .subscribe(
          data => {
            this.p = data;
            this.view = true;
          },
          error => console.log(error)
        )
    }
  }

  verPaciente(): void {
    // Obtener Paciente
    this.PacientesService.getPaciente(this.p.expediente).subscribe(data => {
        this.p = data;

      })
  }



}
