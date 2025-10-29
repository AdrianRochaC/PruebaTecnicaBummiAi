import { Routes } from '@angular/router';
import { SearchComponent } from './components/search/search';
import { FavoritesComponent } from './components/favorites/favorites';

export const routes: Routes = [
  { path: '', redirectTo: 'buscar', pathMatch: 'full' },
  { path: 'buscar', component: SearchComponent },
  { path: 'favoritos', component: FavoritesComponent }
];
