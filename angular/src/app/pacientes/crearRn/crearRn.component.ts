import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { PacientesService } from 'src/app/services/pacientes.service';
import { interval } from 'rxjs';
import { Ipaciente } from 'src/app/models/ipaciente';


@Component({
  selector: 'crearRn',
  templateUrl: './crearRn.component.html',
  styleUrls: ['./crearRn.component.css']
})
export class CrearRnComponent implements OnInit {
  crearRnForm: FormGroup;


  constructor(
    private formBuilder: FormBuilder,
    private pacientesService: PacientesService,
    private router: Router
  ) {
    this.crearRnForm = this.formBuilder.group({
      nombre: ['', Validators.required],
      apellido: ['', Validators.required],
      nacimiento: ['', Validators.required],
      sexo: ['', Validators.required]
    });
  }

  ngOnInit(): void {
    this.NuevoExp();
  }

  NuevoExp() {
    setInterval(() => {
      const nuevoPaciente: Ipaciente = {
        nombre: '',
        apellido: '',
        nacimiento: new Date(),
        sexo: '',
        id: 0,
        expediente: 0,
        dpi: 0,
        pasaporte: '',
        nacionalidad: 0,
        lugar_nacimiento: 0,
        estado_civil: 0,
        educacion: 0,
        pueblo: 0,
        idioma: '',
        ocupacion: '',
        direccion: '',
        telefono: 0,
        email: '',
        padre: '',
        madre: '',
        responsable: '',
        parentesco: 0,
        dpi_responsable: 0,
        telefono_responsable: 0,
        estado: '',
        exp_madre: 0,
        user: '',
        fechaDefuncion: ''
      };
      this.pacientesService.crearPaciente(nuevoPaciente).subscribe(data => {
        this.crearRnForm.patchValue({
          nombre: this.getPrefijo(data.sexo) + data.nombre,
          apellido: data.apellido
        });
      });
    }, 3000);
  }


  getPrefijo(sexo: string): string {
    return sexo === 'M' ? 'hijo de ' : 'hija de ';
  }

  guardarPaciente() {
    if (this.crearRnForm.valid) {
      const nuevoPaciente: Ipaciente = {
        nombre: this.crearRnForm.value.nombre,
        apellido: this.crearRnForm.value.apellido,
        nacimiento: this.crearRnForm.value.nacimiento,
        sexo: this.crearRnForm.value.sexo,
        id: 0,
        expediente: 0,
        dpi: 0,
        pasaporte: '',
        nacionalidad: 0,
        lugar_nacimiento: 0,
        estado_civil: 0,
        educacion: 0,
        pueblo: 0,
        idioma: '',
        ocupacion: '',
        direccion: '',
        telefono: 0,
        email: '',
        padre: '',
        madre: '',
        responsable: '',
        parentesco: 0,
        dpi_responsable: 0,
        telefono_responsable: 0,
        estado: '',
        exp_madre: 0,
        user: '',
        fechaDefuncion: ''
      };

      this.pacientesService.crearPaciente(nuevoPaciente).subscribe(data => {
        this.NuevoExp = data;
        this.router.navigate(['/pacientes']);
      });
    }
  }
}
