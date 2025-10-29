import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class PokemonService {
  constructor(private http: HttpClient) {}

  getPokemon(query: string): Observable<any> {
    return this.http.get(`https://pokeapi.co/api/v2/pokemon/${query.toLowerCase()}`);
  }

  guardarFavorito(pokemon: any): Observable<any> {
    return this.http.post('http://localhost:3000/api/favorites', pokemon);
  }

  getFavoritos() {
    return this.http.get<any[]>('http://localhost:3000/api/favorites');
    }

  eliminarFavorito(nombre: string) {
  return this.http.delete(`http://localhost:3000/api/favorites/${nombre}`);
}


}
