import { Component, OnInit } from '@angular/core';
import { PacientesService } from 'src/app/services/pacientes.service';
import { Ipaciente } from 'src/app/models/ipaciente';
import { Router } from '@angular/router';


@Component({
  selector: 'pacientes',
  templateUrl: './pacientes.component.html',
  styleUrls: ['./pacientes.component.css']
})
export class PacientesComponent{
  public pacientes: Ipaciente[] = [];
  public filteredPacientes: Ipaciente[] = [];
  public searchText: string = '';


  constructor(private pacientesService: PacientesService, private router: Router) { }
  reset: boolean = false;

  ngOnInit() {
    this.getPacientes();
  }

  getPacientes() {
    this.pacientesService.getPacientes().subscribe(data => {
      this.pacientes = data;
      this.filteredPacientes = data;
    });
  }

  delete(exp: number) {
    this.pacientesService.deletePaciente(exp).subscribe(data => {
      this.pacientes = data;
      this.ngOnInit();
    });
  }

  searchPaciente() {
    if (this.searchText) {
      this.filteredPacientes = this.pacientes.filter(paciente =>
        paciente.expediente.toString().includes(this.searchText)
      );
    } else {
      this.filteredPacientes = this.pacientes;
    }
  }


  busqueda: string = '';
  order: string = 'asc';


  sortTable(colu: string) {
    if (this.order === 'asc') {
      this.pacientes.sort((a, b) => a[colu] > b[colu] ? 1 : -1);
      this.order = 'desc';
    } else {
      this.pacientes.sort((a, b) => a[colu] < b[colu] ? 1 : -1);
      this.order = 'asc';
    }
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










