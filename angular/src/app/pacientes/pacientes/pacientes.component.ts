import { Component, OnInit } from '@angular/core';
import { PacientesService } from 'src/app/services/pacientes.service';
import { Ipaciente } from 'src/app/models/ipaciente';
import { ActivatedRoute,Router } from '@angular/router';


@Component({
  selector: 'pacientes',
  templateUrl: './pacientes.component.html',
  styleUrls: ['./pacientes.component.css']
})
export class PacientesComponent{
  public pacientes: Ipaciente[] = []; // Registros a mostrar en la página actual
  public filteredPacientes: Ipaciente[] = [];
  public searchText: string = '';
  public totalRegistros: number = 15; // Total de registros en la lista
  public paginaActual: number = 1; // Página actual


  constructor(private pacientesService: PacientesService, private router: Router, private activateRoute: ActivatedRoute) { }
  reset: boolean = false;

  ngOnInit() {
    this.getPacientes();
  }


  getPacientes() {
    this.pacientesService.getPacientes().subscribe(data => {
      this.pacientes = data.sort((a: { expediente: number; }, b: { expediente: number; }): number => b.expediente - a.expediente);
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


  onPageChange(pageNumber: number) {
    this.paginaActual = pageNumber;
    this.paginarPacientes();
  }

  paginarPacientes() {
    const tamanoPagina = 15;
    const indiceInicio = (this.paginaActual - 1) * tamanoPagina;
    const indiceFin = indiceInicio + tamanoPagina;
    this.filteredPacientes = this.pacientes.slice(indiceInicio, indiceFin);
    this.totalRegistros = this.filteredPacientes.length; // Agrega esta línea para actualizar el número total de registros por página
  }


  getPaginas(): number[] {
    const totalPaginas = Math.ceil(this.filteredPacientes.length / this.totalRegistros);
    return Array.from({ length: totalPaginas }, (_, index) => index + 1);
  }

  totalPaginas(): number {
    return Math.ceil(this.pacientes.length / this.totalRegistros);

  }










}

















