import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule, Routes } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms'; // Importa ReactiveFormsModule
import { FormatoDPIPipe } from './pacientes/pipesPacientes/formatoDPI.pipe';
import { NumberToTextPipe } from './pacientes/pipesPacientes/number-to-text.pipe';




import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { HomeComponent } from './home/home.component';
import { PacientesComponent } from './pacientes/pacientes/pacientes.component';
import { PacienteCrudComponent } from './pacientes/paciente-crud/paciente-crud.component';
import { DetallePacienteComponent } from './pacientes/detallePaciente/detallePaciente.component';

const routes: Routes = [
  { path: '', component: HomeComponent, pathMatch: 'full' },
  { path: 'pacientes', component: PacientesComponent },
  { path: 'paciente-crud', component: PacienteCrudComponent },
  { path: 'paciente/edit/:id', component: PacienteCrudComponent },
  { path: 'detalleP/view/:id', component: DetallePacienteComponent},

]

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    HomeComponent,
    PacientesComponent,
    PacienteCrudComponent,
    PacientesComponent,
    HomeComponent,
    DetallePacienteComponent,
    FormatoDPIPipe,
    NumberToTextPipe,


  ],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    RouterModule.forRoot([
      { path: '', component: HomeComponent, pathMatch: 'full' },
      { path: 'pacientes', component: PacientesComponent },
      { path: 'paciente-crud', component: PacienteCrudComponent },
      { path: 'paciente/edit/:id', component: PacienteCrudComponent },
      { path: 'detalleP/view/:id', component: DetallePacienteComponent},

    ])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

