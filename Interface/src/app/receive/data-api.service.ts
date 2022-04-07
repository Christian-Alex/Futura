import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';

import { Documents } from 'src/app/entities/documents'
import { Clients } from '../entities/clients';
import { Categories } from '../entities/categories';

@Injectable({
  providedIn: 'root'
})
export class DataApiService {
  uri = 'http://127.0.0.1:9000/store/';

  constructor(private http:HttpClient) { }

  httpOption = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  }

  
  handleError(error:any) {
    let errorMessage = '';
    if(error.error instanceof ErrorEvent) {
      errorMessage = error.error.message;
    } else {
      errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
    }
    window.alert(errorMessage);
    return throwError(errorMessage);
  }
  
  getTypeDocuments(): Observable<Documents>{
    return this.http.get<Documents>(this.uri + 'documentos/')
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
  }

  createNewClient(newData:Clients): Observable<Clients> {
    return this.http.post<Clients>(this.uri + "clientes/", JSON.stringify(newData), this.httpOption)
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
  }

  getCategories(): Observable<Categories> {
    return this.http.get<Categories>(this.uri + 'categorias/')
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
  }

  deleteCategorie(id:number): Observable<Categories> {
    return this.http.delete<Categories>(this.uri + 'categorie_info/' + id, this.httpOption)
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
  }

  deleteDocument(id:number): Observable<Documents> {
    return this.http.delete<Documents>(this.uri + 'document_info/' + id, this.httpOption)
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
  }

  createCategorie(newDataCategorie:Categories): Observable<Categories> {
    return this.http.post<Categories>(this.uri + "categorias/" + JSON.stringify(newDataCategorie), this.httpOption)
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
  }

  createDocument(newDataCategorie:Documents): Observable<Documents> {
    return this.http.post<Documents>(this.uri + "documentos/" + JSON.stringify(newDataCategorie), this.httpOption)
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
  }

  modifyCategorie(id:number, dataModify:any): Observable<Categories> {
    return this.http.put<Categories>(this.uri + "categorie_info/" + id, JSON.stringify(dataModify), this.httpOption)
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
  }

  /*
  getTypeDocuments(): Observable<Documents[]> {
    return this.http.get<Documents[]>(this.uri + '/documentos/')
      .pipe(
        tap(data => console.log('All: ', JSON.stringify(data))),
        catchError(this.handleError)
      );
  }

  private handleError(err: HttpErrorResponse): Observable<never> {
    // just a test ... more could would go here
    return throwError(() => err);
  }
*/
}
