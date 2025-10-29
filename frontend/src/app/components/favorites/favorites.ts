import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PokemonService } from '../../services/pokemon.service';
import { PokemonCardComponent } from '../pokemon-card/pokemon-card';

@Component({
  selector: 'app-favorites',
  standalone: true,
  imports: [CommonModule, PokemonCardComponent],
  templateUrl: './favorites.html',
  styleUrls: ['./favorites.scss']
})
export class FavoritesComponent {
  favoritos: any[] = [];
  loading = true;
  error = false;

  constructor(private pokemonService: PokemonService) {
    this.pokemonService.getFavoritos().subscribe({
      next: (data) => {
        this.favoritos = data;
        this.loading = false;
      },
      error: () => {
        this.error = true;
        this.loading = false;
      }
    });
  }

  eliminar(nombre: string) {
    this.favoritos = this.favoritos.filter(p => p.name !== nombre);
  }
}