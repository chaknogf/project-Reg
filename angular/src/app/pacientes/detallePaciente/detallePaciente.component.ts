import { PacienteObjeto } from './../pacienteObjet';
import { interval } from 'rxjs';
import { PacientesService } from './../../services/pacientes.service';
import { Component, OnInit, HostBinding } from '@angular/core';
import { Ipaciente } from 'src/app/models/ipaciente';
import { ActivatedRoute, Router } from '@angular/router';
import { FormGroup, FormBuilder } from '@angular/forms';


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
    idioma: "Español",
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

  };







  view: boolean = false;


  constructor(public PacientesService: PacientesService, private router: Router, private activateRoute: ActivatedRoute, private formBuilder: FormBuilder) {}





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

  calcularEdad(Nacimiento: Date): string {
    const hoy = new Date();
    const fechaNac = new Date(Nacimiento);
    let años = hoy.getFullYear() - fechaNac.getFullYear();
    let meses = hoy.getMonth() - fechaNac.getMonth();
    let dias = hoy.getDate() - fechaNac.getDate();
    if (meses < 0 || (meses === 0 && dias < 0)) {
      años--;
      meses += 12;
      if (dias < 0) {
        meses--;
        dias += new Date(hoy.getFullYear(), hoy.getMonth(), 0).getDate();
      }
    } else if (dias < 0) {
      meses--;
      dias += new Date(hoy.getFullYear(), hoy.getMonth(), 0).getDate();
    }

    return `${años}a ${meses}m ${dias}d`;
  }













}
