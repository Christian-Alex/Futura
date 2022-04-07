import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { DataApiService } from '../receive/data-api.service';

@Component({
  selector: 'app-user-admin',
  templateUrl: './user-admin.component.html',
  styleUrls: ['./user-admin.component.css']
})
export class UserAdminComponent implements OnInit {
  TypeDocuments:any = [];
  Categories:any = [];
  @Input() newDocument = { docId: '10', documentName:"", documentLength:"" }
  @Input() newCategorie = { categorieId: '15', categorieName:'' }

  constructor(private methodsApi:DataApiService, private redireccionamiento:Router) { }

  ngOnInit(): void {
    this.chargeDataCategories();
    this.chargeDataDocuments();

  }

  chargeDataCategories(){
    return this.methodsApi.getCategories().subscribe((data : {}) => {
      this.Categories = data
    })
  }

  chargeDataDocuments(){
    return this.methodsApi.getTypeDocuments().subscribe((data : {}) => {
      this.TypeDocuments = data
    })
  }

  deleteDocument(id:number){
    if(window.confirm('Estás seguro de eliminar el Tipo de Documento?')){
      this.methodsApi.deleteDocument(id).subscribe(() =>{
        this.chargeDataDocuments()
      })
    }
  }

  deleteCategorie(id:number){
    if(window.confirm('Estás seguro de eliminar la Categoria?')){
      this.methodsApi.deleteCategorie(id).subscribe(() =>{
        this.chargeDataCategories()
      })
    }
  }

  createCategorie(){
    this.methodsApi.createCategorie(this.newCategorie).subscribe((data: {}) => {
      this.redireccionamiento.navigate(['/productos'])
    })
  }

  createDocument(){
    this.methodsApi.createDocument(this.newDocument).subscribe((data : {}) => {
      this.redireccionamiento.navigate(['/productos'])
    })
  }


}
