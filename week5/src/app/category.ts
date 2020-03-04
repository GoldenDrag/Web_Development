export interface Category {
    id: number,
    name: string
}

export interface Product {
    categoryId: number,
    id: number,
    name: string,
    href: string,
    description: string
}