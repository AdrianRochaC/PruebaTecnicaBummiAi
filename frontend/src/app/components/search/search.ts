import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { PokemonService } from '../../services/pokemon.service';
import { PokemonCardComponent } from '../pokemon-card/pokemon-card';


@Component({
  selector: 'app-search',
  standalone: true,
  imports: [CommonModule, FormsModule, PokemonCardComponent],
  templateUrl: './search.html',
  styleUrls: ['./search.scss']
})
export class SearchComponent {
  query: string = '';
  loading: boolean = false;
  error: boolean = false;
  pokemon: any | null = null;

  constructor(private pokemonService: PokemonService) {}

  searchPokemon() {
    const value = this.query.trim();
    if (!value) return;

    this.loading = true;
    this.error = false;
    this.pokemon = null;

    this.pokemonService.getPokemon(value).subscribe({
      next: (data) => {
        this.pokemon = data;
        this.loading = false;
      },
      error: () => {
        this.error = true;
        this.loading = false;
      }
    });
  }
}
