import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './home.html',
  styleUrls: ['./home.scss']
})
export class HomeComponent {
  popularPokemon = [
    {
      id: 25,
      name: 'pikachu',
      image: 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png',
      type: 'Electric'
    },
    {
      id: 1,
      name: 'bulbasaur',
      image: 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png',
      type: 'Grass/Poison'
    },
    {
      id: 4,
      name: 'charmander',
      image: 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png',
      type: 'Fire'
    },
    {
      id: 7,
      name: 'squirtle',
      image: 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png',
      type: 'Water'
    },
    {
      id: 150,
      name: 'mewtwo',
      image: 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png',
      type: 'Psychic'
    },
    {
      id: 6,
      name: 'charizard',
      image: 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png',
      type: 'Fire/Flying'
    },
    {
      id: 9,
      name: 'blastoise',
      image: 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png',
      type: 'Water'
    },
    {
      id: 3,
      name: 'venusaur',
      image: 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png',
      type: 'Grass/Poison'
    },
    {
      id: 94,
      name: 'gengar',
      image: 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png',
      type: 'Ghost/Poison'
    },
    {
      id: 143,
      name: 'snorlax',
      image: 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/143.png',
      type: 'Normal'
    }
  ];
}
