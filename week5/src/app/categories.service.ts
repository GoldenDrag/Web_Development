import { Injectable } from '@angular/core';
import { Category, Product } from './category';
import { Observable, of } from 'rxjs';
import { CATEGORIES } from './categories'

@Injectable({
  providedIn: 'root'
})
export class CategoriesService {

  constructor() { }

  getCategories(): Observable<Category[]> {
    return of(CATEGORIES);
  }

  getCategory(id): Observable<Category> {
    return of(CATEGORIES.find(category => category.id === id));
  }
}
