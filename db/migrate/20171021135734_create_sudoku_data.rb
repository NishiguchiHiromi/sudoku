class CreateSudokuData < ActiveRecord::Migration[5.1]
  def change
    create_table :sudoku_data do |t|
      t.string :name

      t.timestamps
    end
  end
end
