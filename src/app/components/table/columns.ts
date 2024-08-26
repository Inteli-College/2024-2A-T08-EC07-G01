import { h } from 'vue'
import { ArrowUpDown, ChevronDown } from 'lucide-vue-next'
import { Button } from '@/components/ui/button'
import type { ColumnDef } from '@tanstack/vue-table'

interface TestData {
    knr: string
    dataPrevisao: string
    falha: string
    tipoFalha: string
    testeIndicado: string
}

export const columns: ColumnDef<TestData>[] = [
    {
        accessorKey: 'knr',
        header: ({ column }) => {
            return h(Button, {
                variant: 'ghost',
                onClick: () => column.toggleSorting(column.getIsSorted() === 'asc'),
            }, () => ['KNR', h(ArrowUpDown, { class: 'ml-2 h-4 w-4' })])
        },
    },
    {
        accessorKey: 'dataPrevisao',
        header: ({ column }) => {
            return h(Button, {
                variant: 'ghost',
                onClick: () => column.toggleSorting(column.getIsSorted() === 'asc'),
            }, () => ['Data de Previsão', h(ArrowUpDown, { class: 'ml-2 h-4 w-4' })])
        },
    },
    {
        accessorKey: 'falha',
        header: ({ column }) => {
            return h(Button, {
                variant: 'ghost',
                onClick: () => column.toggleSorting(column.getIsSorted() === 'asc'),
            }, () => ['Falha', h(ArrowUpDown, { class: 'ml-2 h-4 w-4' })])
        },
    },
    {
        accessorKey: 'tipoFalha',
        header: ({ column }) => {
            return h(Button, {
                variant: 'ghost',
                onClick: () => column.toggleSorting(column.getIsSorted() === 'asc'),
            }, () => ['Tipo de Falha', h(ArrowUpDown, { class: 'ml-2 h-4 w-4' })])
        },
    },
    {
        accessorKey: 'testeIndicado',
        header: ({ column }) => {
            return h(Button, {
                variant: 'ghost',
                onClick: () => column.toggleSorting(column.getIsSorted() === 'asc'),
            }, () => ['Teste Indicado', h(ArrowUpDown, { class: 'ml-2 h-4 w-4' })])
        },
    }
]
