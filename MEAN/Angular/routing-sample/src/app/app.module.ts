import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { LandingComponent } from './landing/landing.component';
import { HomeComponent } from './home/home.component';
import { HomeTaskComponent } from './home-task/home-task.component';
import { Home1Component } from './home/home1/home1.component';
import { Home2Component } from './home/home2/home2.component';


@NgModule({
  declarations: [
    AppComponent,
    LandingComponent,
    HomeComponent,
    HomeTaskComponent,
    Home1Component,
    Home2Component
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
