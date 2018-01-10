import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LandingComponent } from './landing/landing.component';
import { HomeComponent } from './home/home.component';
import { HomeTaskComponent } from './home-task/home-task.component'
import { Home1Component } from './home/home1/home1.component';
import { Home2Component } from './home/home2/home2.component';

const routes: Routes = [
  {path: '', pathMatch: 'full', component: LandingComponent, children: [
      {path:'private', component:Home1Component},
      {path: 'public', component:Home2Component},
    ]},
  {path: 'home/test', pathMatch: 'full', component: HomeComponent, children: []},
  {path: '**', component: HomeTaskComponent, children: []}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
