import { interval } from 'rxjs';
import { PacientesService } from './../../services/pacientes.service';
import { Component, OnInit, HostBinding } from '@angular/core';
import { Ipaciente } from 'src/app/models/ipaciente';
import { ActivatedRoute, Router } from '@angular/router';
import { FormGroup, FormBuilder } from '@angular/forms';

@Component({
  selector: 'paciente-crud',
  templateUrl: './paciente-crud.component.html',
  styleUrls: ['./paciente-crud.component.css']
})
export class PacienteCrudComponent implements OnInit {

  @HostBinding('class') clases = 'row';

  // Objeto del paciente
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

  edit: boolean = false;
  isDead: boolean = false; // Variable para el estado de fallecido (checkbox)

  constructor(public PacientesService: PacientesService, private router: Router, private activateRoute: ActivatedRoute, private formBuilder: FormBuilder) {}

  ngOnInit() {
    // Obtener el expediente del paciente
    //this.NuevoExp()


    // Obtener los parámetros de la ruta
    const params = this.activateRoute.snapshot.params;

    // Verificar si se proporcionó un ID de paciente
    if (params['id']) {
      this.PacientesService.getPaciente(params['id'])
        .subscribe(
          data => {
            this.p = data;
            this.edit = true;
          },
          error => console.log(error)
        )
    }
  }

  crearPaciente(): void {
    // Crear un nuevo paciente
    this.PacientesService.crearPaciente(this.p).subscribe(data => {
        this.p = data;
        this.router.navigate(['/pacientes']);
      })
  }

  editar() {
    // Editar el paciente existente
    this.PacientesService.editPaciente(this.p.expediente, this.p)
      .subscribe(data => {
        this.p = data;
        this.router.navigate(['/pacientes']);
      })
  }

  //Variables para el expediente
  public nuevoExp: number = 0;
  exp = this.NuevoExp()

  NuevoExp() {
    // Obtener el expediente del paciente inicialmente
    this.PacientesService.Expediente().subscribe(data => {
      if (this.edit == false) {
        this.nuevoExp = data;
        this.p.expediente = this.nuevoExp;
      }
    });

    // Actualizar el expediente cada 3 segundos
    // interval(3000).subscribe(() => {
    //   this.PacientesService.Expediente().subscribe(data => {
    //     this.nuevoExp = data;
    //     this.p.expediente = this.nuevoExp;
    //   });
    // });
  }



  cambiarEstado() {

    const confirmacion = confirm('¿Estás seguro de cambiar el estado?');
    if (confirmacion) {
      if (this.p.estado === 'm') {
        this.p.estado = 'v';
      } else {
        this.p.estado = 'm';
        this.p.fechaDefuncion = ""; // Asignar la fecha actual como fecha de defunción
      }
    }
  }




}
