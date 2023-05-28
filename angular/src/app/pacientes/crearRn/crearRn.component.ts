import { Component, OnInit, HostBinding } from '@angular/core';
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

  pacienteExistente: Ipaciente;
  nuevoPaciente: Ipaciente;
  rnForm: FormGroup;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private formBuilder: FormBuilder,
    private pacientesService: PacientesService
  ) {}

  ngOnInit(): void {
    const id = this.route.snapshot.params['id']; // Obtener el ID del registro existente
    this.obtenerPacienteExistente(id); // Obtener los datos del registro existente
    this.inicializarFormulario(); // Inicializar el formulario
  }

  obtenerPacienteExistente(id: number): void {
    this.pacientesService.getPaciente(id).subscribe(
      (data: Ipaciente) => {
        this.pacienteExistente = data; // Guardar los datos del registro existente
      },
      error => {
        console.log(error);
      }
    );
  }

  inicializarFormulario(): void {
    this.rnForm = this.formBuilder.group({
      nombre: ['', Validators.required],
      apellido: ['', Validators.required],
      nacimiento: ['', Validators.required],
      sexo: ['', Validators.required]
    });
  }

  duplicarPaciente(): void {
    if (this.rnForm.valid && this.pacienteExistente) {
      const nombre = this.rnForm.get('nombre').value;
      const apellido = this.rnForm.get('apellido').value;
      const nacimiento = this.rnForm.get('nacimiento').value;
      const sexo = this.rnForm.get('sexo').value;

      this.nuevoPaciente = { ...this.pacienteExistente }; // Duplicar los datos del registro existente
      this.nuevoPaciente.nombre = this.agregarPrefijoNombre(nombre, sexo); // Modificar el nombre con el prefijo correspondiente

      // Guardar el nuevo paciente
      this.pacientesService.crearPaciente(this.nuevoPaciente).subscribe(
        (data: Ipaciente) => {
          this.router.navigate(['/pacientes']); // Redirigir a la lista de pacientes
        },
        error => {
          console.log(error);
        }
      );
    }
  }

  agregarPrefijoNombre(nombre: string, sexo: string): string {
    const prefijo = sexo === 'M' ? 'hijo de ' : 'hija de ';
    return prefijo + nombre;
  }
}
