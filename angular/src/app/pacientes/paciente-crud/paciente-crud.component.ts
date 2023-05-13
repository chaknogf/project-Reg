import { PacientesService } from './../../services/pacientes.service';
import { Component, OnInit, HostBinding } from '@angular/core';
import { Ipaciente } from 'src/app/models/ipaciente';
import { ActivatedRoute, Router } from '@angular/router';


@Component({
  selector: 'paciente-crud',
  templateUrl: './paciente-crud.component.html',
  styleUrls: ['./paciente-crud.component.css']
})
export class PacienteCrudComponent implements OnInit {

  @HostBinding('class') clases = 'row';

  pacientte: Ipaciente = {
    id: 0,
    expediente: 0,
    nombre: "",
    apellido: "",
    dpi: 0,
    pasaporte: "",
    sexo: "",
    nacimiento: new Date("2023-05-11"),
    nacionalidad: 0,
    lugar_nacimiento: 0,
    estado_civil: 0,
    educacion: 0,
    pueblo: 0,
    idioma: "",
    ocupacion: "",
    direccion: "",
    telefono: 0,
    email: "",
    padre: "",
    madre: "",
    responsable: "",
    parentesco: 0,
    dpi_responsable: 0,
    telefono_responsable: 0,
    user: "",
  };

  edit: boolean = false;

  constructor(public PacientesService: PacientesService, private router: Router, private activateRoute: ActivatedRoute) { }
  ngOnInit() {
    const params = this.activateRoute.snapshot.params;
    if (params['expediente']) {
      this.PacientesService.getPaciente(params['expediente'])
        .subscribe(
          data => {
            this.pacientte = data;
            this.edit = true;
          },
          error => console.log(error)
        )
    }
  }

  crearPaciente() {
    this.PacientesService.crearPaciente(this.pacientte)
      .subscribe(data => {
        this.pacientte = data;
        this.router.navigate(['/pacientes']);
    })
  }

  editar() {
    this.PacientesService.editPaciente(this.pacientte.expediente, this.pacientte)
      .subscribe(data => {
        this.pacientte = data;
        this.router.navigate(['/pacientes']);
      })
  }






}
