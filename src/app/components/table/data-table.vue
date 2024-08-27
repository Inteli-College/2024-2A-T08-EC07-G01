<script setup lang="ts" generic="TData, TValue">
import type { ColumnDef, SortingState, ColumnFiltersState, VisibilityState } from '@tanstack/vue-table'

import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'

import {
  FlexRender,
  getCoreRowModel,
  getPaginationRowModel,
  useVueTable,
  getSortedRowModel,
  getFilteredRowModel,
} from '@tanstack/vue-table'

import { valueUpdater } from '@/lib/utils'

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'

const props = defineProps<{
  columns: ColumnDef<TData, TValue>[]
  data: TData[]
}>()

const sorting = ref<SortingState>([])
const columnFilters = ref<ColumnFiltersState>([])
const columnVisibility = ref<VisibilityState>({})

const table = useVueTable({
  get data() { return props.data },
  get columns() { return props.columns },
  getCoreRowModel: getCoreRowModel(),
  getPaginationRowModel: getPaginationRowModel(),
  getSortedRowModel: getSortedRowModel(),
  onSortingChange: updaterOrValue => valueUpdater(updaterOrValue, sorting),
  onColumnSizingChange: updateOrValue => valueUpdater(updateOrValue, columnFilters),
  getFilteredRowModel: getFilteredRowModel(),
  onColumnVisibilityChange: updaterOrValue => valueUpdater(updaterOrValue, columnVisibility),
  state: {
    get sorting() { return sorting.value },
    get columnVisibility() { return columnVisibility.value },
  }
})
</script>

<template>
<div>
    <div class="flex items-center py-4">
    
        <div class="relative max-w-sm w-full transition-transform duration-300 ease-in-out transform focus-within:scale-105 focus-within:shadow-lg">
    <Icon 
      :name="'mdi:magnify'"
      class="absolute left-3 top-1/2 transform -translate-y-1/2 text-xl text-customBlue transition duration-300 ease-in-out"
    />
    
    <Input
      class="pl-10 w-full"
      placeholder="Filtrar..."
      :model-value="table.getColumn('tipoFalha')?.getFilterValue() as string"
      @update:model-value="table.getColumn('tipoFalha')?.setFilterValue($event)"
    />
  </div>
    
    
    <DropdownMenu class="ml-4">
      <DropdownMenuTrigger as-child>
        <Button variant="outline" class="ml-auto transition duration-300 ease-in-out overflow-hidden text-black hover:text-white hover:scale-[103%] hover:bg-customBlue">
            <Icon :name="'mdi:format-columns'" class="mr-1"/>
            Colunas
          <ChevronDown class="w-4 h-4 ml-2" />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <DropdownMenuCheckboxItem
          v-for="column in table.getAllColumns().filter((column) => column.getCanHide())" 
          :key="column.id"
          class="capitalize"
          :checked="column.getIsVisible()" 
          @update:checked="(value) => {
            column.toggleVisibility(!!value)
          }"
        >
          {{ column.id }}
        </DropdownMenuCheckboxItem>
      </DropdownMenuContent>
    </DropdownMenu>
  </div>
  <div class="border rounded-md">
    <Table>
      <TableHeader>
        <TableRow v-for="headerGroup in table.getHeaderGroups()" :key="headerGroup.id">
          <TableHead v-for="header in headerGroup.headers" :key="header.id">
            <FlexRender
              v-if="!header.isPlaceholder" :render="header.column.columnDef.header"
              :props="header.getContext()"
            />
          </TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        <template v-if="table.getRowModel().rows?.length">
          <TableRow
            v-for="row in table.getRowModel().rows" :key="row.id"
            :data-state="row.getIsSelected() ? 'selected' : undefined"
          >
            <TableCell v-for="cell in row.getVisibleCells()" :key="cell.id">
              <FlexRender :render="cell.column.columnDef.cell" :props="cell.getContext()" />
            </TableCell>
          </TableRow>
        </template>
        <template v-else>
          <TableRow>
            <TableCell :colspan="columns.length" class="h-24 text-center">
              No results.
            </TableCell>
          </TableRow>
        </template>
      </TableBody>
    </Table>
  </div>
  <div class="flex items-center justify-end py-4 space-x-2">
<Button
    variant="outline"
    size="sm"
    :disabled="!table.getCanPreviousPage()"
    @click="table.previousPage()"
    class="relative group bg-transparent overflow-hidden text-black hover:text-white transition-all duration-300"
>
    <span class="absolute inset-0 w-full h-full bg-customBlue transform scale-x-0 group-hover:scale-x-100 origin-right transition duration-300 ease-in-out"></span>
    <span class="relative z-10 flex items-center">
        <Icon :name="'mdi:navigate-before'" class="mr-1 group-hover:text-white transition duration-300 ease-in-out" />
        Anterior
    </span>
</Button>

<Button
    variant="outline"
    size="sm"
    :disabled="!table.getCanNextPage()"
    @click="table.nextPage()"
    class="relative group bg-transparent overflow-hidden text-black hover:text-white transition-all duration-300"
>
    <span class="absolute inset-0 w-full h-full bg-customBlue transform scale-x-0 group-hover:scale-x-100 origin-left transition duration-300 ease-in-out"></span>
    <span class="relative z-10 flex items-center">
        Próxima
        <Icon :name="'mdi:navigate-next'" class="ml-1 group-hover:text-white transition duration-300 ease-in-out" />
    </span>
</Button>




  </div>
</div>
</template>