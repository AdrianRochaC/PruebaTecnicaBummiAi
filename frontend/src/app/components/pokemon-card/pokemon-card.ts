import { Component, EventEmitter, Input, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PokemonService } from '../../services/pokemon.service';

@Component({
  selector: 'app-pokemon-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './pokemon-card.html',
  styleUrls: ['./pokemon-card.scss']
})
export class PokemonCardComponent {
  @Input() pokemon: any;
  @Output() eliminado = new EventEmitter<string>();

  favoritos: string[] = [];

  constructor(private pokemonService: PokemonService) {}

  ngOnInit() {
    this.pokemonService.getFavoritos().subscribe({
      next: (data) => {
        this.favoritos = data.map((f: any) => f.name.toLowerCase());
      }
    });
  }

  get yaEsFavorito(): boolean {
    return this.favoritos.includes(this.pokemon.name.toLowerCase());
  }

  guardarFavorito() {
    const favorito = {
      name: this.pokemon.name,
      image: this.pokemon.sprites.front_default,
      nickname: '',
    };

    this.pokemonService.guardarFavorito(favorito).subscribe({
      next: () => {
        alert('¡Guardado como Favorito!');
        this.favoritos.push(this.pokemon.name.toLowerCase());
      },
      error: () => alert('Error al guardar el favorito')
    });
  }

  eliminarFavorito() {
    console.log('Botón eliminar presionado:', this.pokemon.name);
    this.pokemonService.eliminarFavorito(this.pokemon.name).subscribe({
      next: () => {
        alert('Eliminado de favoritos');
        this.favoritos = this.favoritos.filter(n => n !== this.pokemon.name.toLowerCase());
        this.eliminado.emit(this.pokemon.name);
      },
      error: () => alert('Error al eliminar el favorito')
    });
  }
}
