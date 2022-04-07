import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { DataApiService } from '../receive/data-api.service';

@Component({
  selector: 'app-user-register',
  templateUrl: './user-register.component.html',
  styleUrls: ['./user-register.component.css']
})
export class UserRegisterComponent implements OnInit {
  @Input() newClient = { clientId:'0', fullName:'', typeDoc:'', numDoc:'', phoneNumber:'', email:'', password:'', dateBirth:'', address:'', rules:["USER"], dateRegister:'', debitCard:'987123412341234123408/12', active:'1'}
  TypeDocuments:any = []

  constructor(public methodsApi:DataApiService, private redireccion:Router) { }

  extractDateCurrent(): string{
    let fullDate: Date = new Date();
    let year = fullDate.getFullYear();  
    let month = fullDate.getMonth() + parseInt("1");  
    let day = fullDate.getDate();  
    return year + "-" + month + "-" + day
  }

  ngOnInit(): void {
    this.chargeTypeDocuments();
    this.extractDateCurrent()
  }

  chargeTypeDocuments(){
    return this.methodsApi.getTypeDocuments().subscribe((data : {}) => {
      this.TypeDocuments = data
    })
  }

  create(){
    Object.entries(this.newClient).forEach(([key, value]) => {
      console.log(value)
    });
  }

  createNewClient(){
    this.newClient.dateRegister = this.extractDateCurrent();
    this.methodsApi.createNewClient(this.newClient).subscribe((data: {}) => {
      this.redireccion.navigate(['/productos'])
      alert("se envio data")
    })
  }
}
