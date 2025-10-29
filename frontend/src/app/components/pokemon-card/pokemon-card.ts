import { Component, EventEmitter, Input, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';  // ← AGREGAR ESTE IMPORT
import { PokemonService } from '../../services/pokemon.service';

@Component({
  selector: 'app-pokemon-card',
  standalone: true,
  imports: [CommonModule, FormsModule],  // ← AGREGAR FormsModule
  templateUrl: './pokemon-card.html',
  styleUrls: ['./pokemon-card.scss']
})
export class PokemonCardComponent {
  @Input() pokemon: any;
  @Output() eliminado = new EventEmitter<string>();

  favoritos: string[] = [];
  eliminando = false;
  editandoApodo = false;
  nuevoApodo = '';

  constructor(private pokemonService: PokemonService) {}

  ngOnInit() {
    this.pokemonService.getFavoritos().subscribe({
      next: (data) => {
        this.favoritos = data.map((f: any) => f.name);
      }
    });
  }

  get yaEsFavorito(): boolean {
    return this.favoritos.includes(this.pokemon.name);
  }

  guardarFavorito() {
    if (!this.pokemon || !this.pokemon.id || !this.pokemon.name) {
      alert('Error: Datos del Pokémon incompletos');
      return;
    }

    const favorito = {
      id: this.pokemon.id,
      name: this.pokemon.name,
      image: this.pokemon.sprites?.front_default || this.pokemon.image || '',
      nickname: '',
    };

    this.pokemonService.guardarFavorito(favorito).subscribe({
      next: () => {
        alert('Guardado como Favorito');
        this.favoritos.push(this.pokemon.name);
      },
      error: () => alert('Error al guardar el favorito')
    });
  }

  eliminarFavorito() {
    if (this.eliminando) return;
    
    this.eliminando = true;
    
    this.pokemonService.eliminarFavorito(this.pokemon.name).subscribe({
      next: () => {
        alert('Eliminado de favoritos');
        this.favoritos = this.favoritos.filter(n => n !== this.pokemon.name);
        this.eliminado.emit(this.pokemon.name);
        this.eliminando = false;
      },
      error: () => {
        alert('Error al eliminar el favorito');
        this.eliminando = false;
      }
    });
  }

  iniciarEdicionApodo() {
    this.editandoApodo = true;
    this.nuevoApodo = this.pokemon.nickname || '';
  }

  cancelarEdicionApodo() {
    this.editandoApodo = false;
    this.nuevoApodo = '';
  }

  guardarApodo() {
    if (!this.nuevoApodo.trim()) return;
    
    if (!this.pokemon.name) {
      alert('Error: No se puede identificar el Pokémon');
      return;
    }
    
    this.pokemonService.actualizarApodo(this.pokemon.name, this.nuevoApodo.trim()).subscribe({
      next: () => {
        this.pokemon.nickname = this.nuevoApodo.trim();
        this.editandoApodo = false;
        this.nuevoApodo = '';
        alert('Apodo guardado exitosamente');
      },
      error: () => {
        alert('Error al guardar el apodo');
      }
    });
  }
}