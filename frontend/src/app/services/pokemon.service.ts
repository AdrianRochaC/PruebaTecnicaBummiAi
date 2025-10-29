import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class PokemonService {
  private apiUrl = 'https://pokedex-backend-1ybj.onrender.com';
  
  constructor(private http: HttpClient) {}

  getPokemon(query: string): Observable<any> {
    return this.http.get(`https://pokeapi.co/api/v2/pokemon/${query.toLowerCase()}`);
  }

  guardarFavorito(pokemon: any): Observable<any> {
    const favorito = {
      id: pokemon.id,
      name: pokemon.name,
      image: pokemon.sprites?.front_default || pokemon.image || '',
      nickname: '',
    };
    return this.http.post(`${this.apiUrl}/api/favorites`, favorito);
  }

  getFavoritos() {
    return this.http.get<any[]>(`${this.apiUrl}/api/favorites`);
  }

  eliminarFavorito(nombre: string) {
    return this.http.delete(`${this.apiUrl}/api/favorites/${nombre}`);
  }

  actualizarApodo(nombre: string, nickname: string): Observable<any> {
    return this.http.put(`${this.apiUrl}/api/favorites/${nombre}`, { nickname });
  }
}