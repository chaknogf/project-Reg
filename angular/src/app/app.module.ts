import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule, Routes } from '@angular/router';



import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { HomeComponent } from './home/home.component';
import { PacientesComponent } from './pacientes/pacientes/pacientes.component';
import { PacienteCrudComponent } from './pacientes/paciente-crud/paciente-crud.component';


const routes: Routes = [
  { path: '', component: HomeComponent, pathMatch: 'full' },
  { path: 'pacientes', component: PacientesComponent },
  { path: 'paciente-crud', component: PacienteCrudComponent },
  { path: 'paciente/edit/:id', component: PacienteCrudComponent}
]

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    HomeComponent,
    PacientesComponent,
    PacienteCrudComponent,
    PacientesComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule.forRoot([
      { path: '', component: HomeComponent, pathMatch: 'full' },
      { path: 'pacientes', component: PacientesComponent },
      { path: 'paciente-crud', component: PacienteCrudComponent },
      { path: 'paciente/edit/:id', component: PacienteCrudComponent}
    ])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

