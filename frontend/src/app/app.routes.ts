import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home';
import { SearchComponent } from './components/search/search';
import { FavoritesComponent } from './components/favorites/favorites';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'inicio', component: HomeComponent },
  { path: 'buscar', component: SearchComponent },
  { path: 'favoritos', component: FavoritesComponent }
];
