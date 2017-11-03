class CreateSudokuDbs < ActiveRecord::Migration[5.1]
  def change
    create_table :sudoku_dbs do |t|
      t.string :name

      t.timestamps
    end
  end
end
