import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes} from '@angular/router';
import { CategoriesComponent } from './categories/categories.component';


const routes: Routes = [
  { path:'categories', component: CategoriesComponent},
  { path:'categories/:id', component: }
]
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
